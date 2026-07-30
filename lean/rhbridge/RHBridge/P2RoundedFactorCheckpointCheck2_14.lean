import RHBridge.P2RoundedFactorCheckpointData2

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel2FactorChunk14 :
    P2RoundedFactorCheckpointData.panel2Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨2, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel2Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨2, by decide⟩ := by
  decide +kernel

theorem panel2Prefix56_eq :
    P2RoundedFactorCheckpointData.panel2Prefix56 =
      normalizedPrefixTermAtomApprox ⟨56, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk14.1

theorem panel2Prefix57_eq :
    P2RoundedFactorCheckpointData.panel2Prefix57 =
      normalizedPrefixTermAtomApprox ⟨57, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk14.2.1

theorem panel2Prefix58_eq :
    P2RoundedFactorCheckpointData.panel2Prefix58 =
      normalizedPrefixTermAtomApprox ⟨58, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk14.2.2.1

theorem panel2Prefix59_eq :
    P2RoundedFactorCheckpointData.panel2Prefix59 =
      normalizedPrefixTermAtomApprox ⟨59, by decide⟩ ⟨2, by decide⟩ := by
  exact panel2FactorChunk14.2.2.2

end RHP2Bridge
