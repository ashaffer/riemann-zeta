import RHBridge.P2RoundedFactorCheckpointData1

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel1FactorChunk2 :
    P2RoundedFactorCheckpointData.panel1Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨1, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel1Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨1, by decide⟩ := by
  decide +kernel

theorem panel1Prefix8_eq :
    P2RoundedFactorCheckpointData.panel1Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk2.1

theorem panel1Prefix9_eq :
    P2RoundedFactorCheckpointData.panel1Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk2.2.1

theorem panel1Prefix10_eq :
    P2RoundedFactorCheckpointData.panel1Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk2.2.2.1

theorem panel1Prefix11_eq :
    P2RoundedFactorCheckpointData.panel1Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨1, by decide⟩ := by
  exact panel1FactorChunk2.2.2.2

end RHP2Bridge
