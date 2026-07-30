import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk14 :
    P2RoundedFactorCheckpointData.panel23Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix56_eq :
    P2RoundedFactorCheckpointData.panel23Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk14.1

theorem panel23Prefix57_eq :
    P2RoundedFactorCheckpointData.panel23Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk14.2.1

theorem panel23Prefix58_eq :
    P2RoundedFactorCheckpointData.panel23Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk14.2.2.1

theorem panel23Prefix59_eq :
    P2RoundedFactorCheckpointData.panel23Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk14.2.2.2

end RHP2Bridge
