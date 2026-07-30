import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk7 :
    P2RoundedFactorCheckpointData.panel14Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix28_eq :
    P2RoundedFactorCheckpointData.panel14Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk7.1

theorem panel14Prefix29_eq :
    P2RoundedFactorCheckpointData.panel14Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk7.2.1

theorem panel14Prefix30_eq :
    P2RoundedFactorCheckpointData.panel14Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk7.2.2.1

theorem panel14Prefix31_eq :
    P2RoundedFactorCheckpointData.panel14Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk7.2.2.2

end RHP2Bridge
