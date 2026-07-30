import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk4 :
    P2RoundedFactorCheckpointData.panel1Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix16_eq :
    P2RoundedFactorCheckpointData.panel1Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk4.1

theorem panel1Prefix17_eq :
    P2RoundedFactorCheckpointData.panel1Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk4.2.1

theorem panel1Prefix18_eq :
    P2RoundedFactorCheckpointData.panel1Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk4.2.2.1

theorem panel1Prefix19_eq :
    P2RoundedFactorCheckpointData.panel1Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk4.2.2.2

end RHP2Bridge
