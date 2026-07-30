import RHBridge.P2RoundedFactorCheckpointData9

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel9FactorChunk7 :
    P2RoundedFactorCheckpointData.panel9Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨9, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel9Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨9, by decide⟩ := by
  decide +kernel

theorem panel9Prefix28_eq :
    P2RoundedFactorCheckpointData.panel9Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk7.1

theorem panel9Prefix29_eq :
    P2RoundedFactorCheckpointData.panel9Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk7.2.1

theorem panel9Prefix30_eq :
    P2RoundedFactorCheckpointData.panel9Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk7.2.2.1

theorem panel9Prefix31_eq :
    P2RoundedFactorCheckpointData.panel9Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨9, by decide⟩ := by
  exact panel9FactorChunk7.2.2.2

end RHP2Bridge
