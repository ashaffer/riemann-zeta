import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk7 :
    P2RoundedFactorCheckpointData.panel8Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix28_eq :
    P2RoundedFactorCheckpointData.panel8Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk7.1

theorem panel8Prefix29_eq :
    P2RoundedFactorCheckpointData.panel8Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk7.2.1

theorem panel8Prefix30_eq :
    P2RoundedFactorCheckpointData.panel8Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk7.2.2.1

theorem panel8Prefix31_eq :
    P2RoundedFactorCheckpointData.panel8Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk7.2.2.2

end RHP2Bridge
