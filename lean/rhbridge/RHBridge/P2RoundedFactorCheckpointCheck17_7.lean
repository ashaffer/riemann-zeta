import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk7 :
    P2RoundedFactorCheckpointData.panel17Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix28_eq :
    P2RoundedFactorCheckpointData.panel17Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk7.1

theorem panel17Prefix29_eq :
    P2RoundedFactorCheckpointData.panel17Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk7.2.1

theorem panel17Prefix30_eq :
    P2RoundedFactorCheckpointData.panel17Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk7.2.2.1

theorem panel17Prefix31_eq :
    P2RoundedFactorCheckpointData.panel17Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk7.2.2.2

end RHP2Bridge
