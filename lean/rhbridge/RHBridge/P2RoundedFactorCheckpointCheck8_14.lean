import RHBridge.P2RoundedFactorCheckpointData8

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel8FactorChunk14 :
    P2RoundedFactorCheckpointData.panel8Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨8, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel8Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨8, by decide⟩ := by
  decide +kernel

theorem panel8Prefix56_eq :
    P2RoundedFactorCheckpointData.panel8Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk14.1

theorem panel8Prefix57_eq :
    P2RoundedFactorCheckpointData.panel8Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk14.2.1

theorem panel8Prefix58_eq :
    P2RoundedFactorCheckpointData.panel8Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk14.2.2.1

theorem panel8Prefix59_eq :
    P2RoundedFactorCheckpointData.panel8Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨8, by decide⟩ := by
  exact panel8FactorChunk14.2.2.2

end RHP2Bridge
