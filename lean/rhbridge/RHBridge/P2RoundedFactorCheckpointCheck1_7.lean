import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk7 :
    P2RoundedFactorCheckpointData.panel1Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix28_eq :
    P2RoundedFactorCheckpointData.panel1Prefix28 =
      normalizedPrefixTermAtomApprox ⟨28, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk7.1

theorem panel1Prefix29_eq :
    P2RoundedFactorCheckpointData.panel1Prefix29 =
      normalizedPrefixTermAtomApprox ⟨29, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk7.2.1

theorem panel1Prefix30_eq :
    P2RoundedFactorCheckpointData.panel1Prefix30 =
      normalizedPrefixTermAtomApprox ⟨30, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk7.2.2.1

theorem panel1Prefix31_eq :
    P2RoundedFactorCheckpointData.panel1Prefix31 =
      normalizedPrefixTermAtomApprox ⟨31, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk7.2.2.2

end RHP2Bridge
