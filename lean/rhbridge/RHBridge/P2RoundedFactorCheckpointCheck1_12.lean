import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk12 :
    P2RoundedFactorCheckpointData.panel1Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix48_eq :
    P2RoundedFactorCheckpointData.panel1Prefix48 =
      normalizedPrefixTermAtomApprox ⟨48, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk12.1

theorem panel1Prefix49_eq :
    P2RoundedFactorCheckpointData.panel1Prefix49 =
      normalizedPrefixTermAtomApprox ⟨49, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk12.2.1

theorem panel1Prefix50_eq :
    P2RoundedFactorCheckpointData.panel1Prefix50 =
      normalizedPrefixTermAtomApprox ⟨50, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk12.2.2.1

theorem panel1Prefix51_eq :
    P2RoundedFactorCheckpointData.panel1Prefix51 =
      normalizedPrefixTermAtomApprox ⟨51, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk12.2.2.2

end RHP2Bridge
