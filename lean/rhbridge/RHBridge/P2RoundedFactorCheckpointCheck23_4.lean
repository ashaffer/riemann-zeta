import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk4 :
    P2RoundedFactorCheckpointData.panel23Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix16_eq :
    P2RoundedFactorCheckpointData.panel23Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk4.1

theorem panel23Prefix17_eq :
    P2RoundedFactorCheckpointData.panel23Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk4.2.1

theorem panel23Prefix18_eq :
    P2RoundedFactorCheckpointData.panel23Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk4.2.2.1

theorem panel23Prefix19_eq :
    P2RoundedFactorCheckpointData.panel23Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk4.2.2.2

end RHP2Bridge
