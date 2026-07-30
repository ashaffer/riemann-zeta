import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk7 :
    P2RoundedFactorCheckpointData.panel23Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix28_eq :
    P2RoundedFactorCheckpointData.panel23Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk7.1

theorem panel23Prefix29_eq :
    P2RoundedFactorCheckpointData.panel23Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk7.2.1

theorem panel23Prefix30_eq :
    P2RoundedFactorCheckpointData.panel23Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk7.2.2.1

theorem panel23Prefix31_eq :
    P2RoundedFactorCheckpointData.panel23Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk7.2.2.2

end RHP2Bridge
