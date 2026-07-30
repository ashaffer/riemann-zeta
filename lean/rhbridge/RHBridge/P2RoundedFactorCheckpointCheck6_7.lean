import RHBridge.P2RoundedFactorCheckpointData6

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel6FactorChunk7 :
    P2RoundedFactorCheckpointData.panel6Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨6, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel6Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨6, by decide⟩ := by
  decide +kernel

theorem panel6Prefix28_eq :
    P2RoundedFactorCheckpointData.panel6Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk7.1

theorem panel6Prefix29_eq :
    P2RoundedFactorCheckpointData.panel6Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk7.2.1

theorem panel6Prefix30_eq :
    P2RoundedFactorCheckpointData.panel6Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk7.2.2.1

theorem panel6Prefix31_eq :
    P2RoundedFactorCheckpointData.panel6Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨6, by decide⟩ := by
  exact panel6FactorChunk7.2.2.2

end RHP2Bridge
