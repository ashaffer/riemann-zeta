import RHBridge.P2RoundedFactorCheckpointData13

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel13FactorChunk7 :
    P2RoundedFactorCheckpointData.panel13Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨13, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel13Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨13, by decide⟩ := by
  decide +kernel

theorem panel13Prefix28_eq :
    P2RoundedFactorCheckpointData.panel13Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk7.1

theorem panel13Prefix29_eq :
    P2RoundedFactorCheckpointData.panel13Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk7.2.1

theorem panel13Prefix30_eq :
    P2RoundedFactorCheckpointData.panel13Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk7.2.2.1

theorem panel13Prefix31_eq :
    P2RoundedFactorCheckpointData.panel13Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨13, by decide⟩ := by
  exact panel13FactorChunk7.2.2.2

end RHP2Bridge
