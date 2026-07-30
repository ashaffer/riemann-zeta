import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk7 :
    P2RoundedFactorCheckpointData.panel0Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix28_eq :
    P2RoundedFactorCheckpointData.panel0Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk7.1

theorem panel0Prefix29_eq :
    P2RoundedFactorCheckpointData.panel0Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk7.2.1

theorem panel0Prefix30_eq :
    P2RoundedFactorCheckpointData.panel0Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk7.2.2.1

theorem panel0Prefix31_eq :
    P2RoundedFactorCheckpointData.panel0Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk7.2.2.2

end RHP2Bridge
