import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk2 :
    P2RoundedFactorCheckpointData.panel2Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix8_eq :
    P2RoundedFactorCheckpointData.panel2Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk2.1

theorem panel2Prefix9_eq :
    P2RoundedFactorCheckpointData.panel2Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk2.2.1

theorem panel2Prefix10_eq :
    P2RoundedFactorCheckpointData.panel2Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk2.2.2.1

theorem panel2Prefix11_eq :
    P2RoundedFactorCheckpointData.panel2Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk2.2.2.2

end RHP2Bridge
