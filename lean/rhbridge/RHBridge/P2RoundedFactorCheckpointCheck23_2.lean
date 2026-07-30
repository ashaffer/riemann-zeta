import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk2 :
    P2RoundedFactorCheckpointData.panel23Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix8_eq :
    P2RoundedFactorCheckpointData.panel23Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk2.1

theorem panel23Prefix9_eq :
    P2RoundedFactorCheckpointData.panel23Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk2.2.1

theorem panel23Prefix10_eq :
    P2RoundedFactorCheckpointData.panel23Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk2.2.2.1

theorem panel23Prefix11_eq :
    P2RoundedFactorCheckpointData.panel23Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk2.2.2.2

end RHP2Bridge
