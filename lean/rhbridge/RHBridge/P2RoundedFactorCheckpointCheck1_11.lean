import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk11 :
    P2RoundedFactorCheckpointData.panel1Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix44_eq :
    P2RoundedFactorCheckpointData.panel1Prefix44 =
      normalizedPrefixTermAtomApprox ⟨44, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk11.1

theorem panel1Prefix45_eq :
    P2RoundedFactorCheckpointData.panel1Prefix45 =
      normalizedPrefixTermAtomApprox ⟨45, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk11.2.1

theorem panel1Prefix46_eq :
    P2RoundedFactorCheckpointData.panel1Prefix46 =
      normalizedPrefixTermAtomApprox ⟨46, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk11.2.2.1

theorem panel1Prefix47_eq :
    P2RoundedFactorCheckpointData.panel1Prefix47 =
      normalizedPrefixTermAtomApprox ⟨47, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk11.2.2.2

end RHP2Bridge
