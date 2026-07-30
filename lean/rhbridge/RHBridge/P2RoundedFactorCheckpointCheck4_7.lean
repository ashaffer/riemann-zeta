import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk7 :
    P2RoundedFactorCheckpointData.panel4Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix28_eq :
    P2RoundedFactorCheckpointData.panel4Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk7.1

theorem panel4Prefix29_eq :
    P2RoundedFactorCheckpointData.panel4Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk7.2.1

theorem panel4Prefix30_eq :
    P2RoundedFactorCheckpointData.panel4Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk7.2.2.1

theorem panel4Prefix31_eq :
    P2RoundedFactorCheckpointData.panel4Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk7.2.2.2

end RHP2Bridge
