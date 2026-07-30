import RHBridge.P2RoundedFactorCheckpointData25

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel25FactorChunk7 :
    P2RoundedFactorCheckpointData.panel25Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨25, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel25Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨25, by decide⟩ := by
  decide +kernel

theorem panel25Prefix28_eq :
    P2RoundedFactorCheckpointData.panel25Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk7.1

theorem panel25Prefix29_eq :
    P2RoundedFactorCheckpointData.panel25Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk7.2.1

theorem panel25Prefix30_eq :
    P2RoundedFactorCheckpointData.panel25Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk7.2.2.1

theorem panel25Prefix31_eq :
    P2RoundedFactorCheckpointData.panel25Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨25, by decide⟩ := by
  exact panel25FactorChunk7.2.2.2

end RHP2Bridge
