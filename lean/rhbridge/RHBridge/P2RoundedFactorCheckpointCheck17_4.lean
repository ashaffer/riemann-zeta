import RHBridge.P2RoundedFactorCheckpointData17

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FactorChunk4 :
    P2RoundedFactorCheckpointData.panel17Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨17, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel17Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨17, by decide⟩ := by
  decide +kernel

theorem panel17Prefix16_eq :
    P2RoundedFactorCheckpointData.panel17Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk4.1

theorem panel17Prefix17_eq :
    P2RoundedFactorCheckpointData.panel17Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk4.2.1

theorem panel17Prefix18_eq :
    P2RoundedFactorCheckpointData.panel17Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk4.2.2.1

theorem panel17Prefix19_eq :
    P2RoundedFactorCheckpointData.panel17Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨17, by decide⟩ := by
  exact panel17FactorChunk4.2.2.2

end RHP2Bridge
