import RHBridge.P2RoundedFactorCheckpointData7

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel7FactorChunk7 :
    P2RoundedFactorCheckpointData.panel7Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨7, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel7Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨7, by decide⟩ := by
  decide +kernel

theorem panel7Prefix28_eq :
    P2RoundedFactorCheckpointData.panel7Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk7.1

theorem panel7Prefix29_eq :
    P2RoundedFactorCheckpointData.panel7Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk7.2.1

theorem panel7Prefix30_eq :
    P2RoundedFactorCheckpointData.panel7Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk7.2.2.1

theorem panel7Prefix31_eq :
    P2RoundedFactorCheckpointData.panel7Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨7, by decide⟩ := by
  exact panel7FactorChunk7.2.2.2

end RHP2Bridge
