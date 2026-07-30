import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk7 :
    P2RoundedFactorCheckpointData.panel2Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix28_eq :
    P2RoundedFactorCheckpointData.panel2Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk7.1

theorem panel2Prefix29_eq :
    P2RoundedFactorCheckpointData.panel2Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk7.2.1

theorem panel2Prefix30_eq :
    P2RoundedFactorCheckpointData.panel2Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk7.2.2.1

theorem panel2Prefix31_eq :
    P2RoundedFactorCheckpointData.panel2Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk7.2.2.2

end RHP2Bridge
