import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk9 :
    P2RoundedFactorCheckpointData.panel1Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix36_eq :
    P2RoundedFactorCheckpointData.panel1Prefix36 =
      normalizedPrefixTermAtomApprox ⟨36, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk9.1

theorem panel1Prefix37_eq :
    P2RoundedFactorCheckpointData.panel1Prefix37 =
      normalizedPrefixTermAtomApprox ⟨37, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk9.2.1

theorem panel1Prefix38_eq :
    P2RoundedFactorCheckpointData.panel1Prefix38 =
      normalizedPrefixTermAtomApprox ⟨38, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk9.2.2.1

theorem panel1Prefix39_eq :
    P2RoundedFactorCheckpointData.panel1Prefix39 =
      normalizedPrefixTermAtomApprox ⟨39, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk9.2.2.2

end RHP2Bridge
